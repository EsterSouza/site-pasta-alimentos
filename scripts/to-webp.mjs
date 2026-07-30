#!/usr/bin/env node
/**
 * to-webp.mjs — converte imagens raster (png/jpg/jpeg) para WebP.
 *
 * Uso:
 *   node scripts/to-webp.mjs <arquivo|pasta> [...]   # avulso ou em lote
 *   node scripts/to-webp.mjs public                  # converte tudo em public/
 *   (sem args, o lint-staged passa os arquivos staged)
 *
 * Comportamento:
 *   - Converte cada raster → .webp (mesmo basename, mesma pasta), quality 80, effort 6.
 *   - Remove o arquivo raster original.
 *   - Faz o stage no git (novo .webp + remoção do original), para o pre-commit.
 *   - Ignora .svg/.gif (vetor/animado) e qualquer coisa que não seja png/jpg/jpeg.
 *   - Idempotente: se não houver raster, não faz nada.
 *
 * Requer: sharp (devDependency). Git é opcional (desliga com NO_GIT=1).
 */
import { readdir, stat, readFile, writeFile, rm } from "node:fs/promises"
import { join, extname, dirname, basename } from "node:path"
import { execFileSync } from "node:child_process"

const RASTER = new Set([".png", ".jpg", ".jpeg"])
const QUALITY = 80
const EFFORT = 6

let sharp
try {
  sharp = (await import("sharp")).default
} catch {
  console.error("[to-webp] Falta a dependência 'sharp'. Instale: npm i -D sharp")
  process.exit(1)
}

const useGit = process.env.NO_GIT !== "1"

function git(args) {
  if (!useGit) return
  try {
    execFileSync("git", args, { stdio: "ignore" })
  } catch {
    /* fora de repo git ou arquivo não rastreado — silencioso */
  }
}

async function walk(path) {
  const out = []
  const st = await stat(path).catch(() => null)
  if (!st) return out
  if (st.isDirectory()) {
    for (const entry of await readdir(path)) {
      out.push(...(await walk(join(path, entry))))
    }
  } else if (RASTER.has(extname(path).toLowerCase())) {
    out.push(path)
  }
  return out
}

async function convert(src) {
  const dest = join(dirname(src), basename(src, extname(src)) + ".webp")
  const input = await readFile(src)
  const output = await sharp(input).webp({ quality: QUALITY, effort: EFFORT }).toBuffer()
  await writeFile(dest, output)
  await rm(src)
  git(["add", dest]) // adiciona o novo .webp
  git(["add", src]) // "add" de arquivo deletado = staging da remoção
  const kb = (n) => (n / 1024).toFixed(0)
  console.log(`[to-webp] ${src} → ${dest}  (${kb(input.length)}KB → ${kb(output.length)}KB)`)
  return { before: input.length, after: output.length }
}

const args = process.argv.slice(2)
if (args.length === 0) {
  console.log("[to-webp] nada a converter (sem arquivos/pastas nos args).")
  process.exit(0)
}

const targets = []
for (const a of args) targets.push(...(await walk(a)))

if (targets.length === 0) {
  console.log("[to-webp] nenhum raster (png/jpg/jpeg) encontrado.")
  process.exit(0)
}

let before = 0
let after = 0
for (const src of targets) {
  try {
    const r = await convert(src)
    before += r.before
    after += r.after
  } catch (e) {
    console.error(`[to-webp] ERRO em ${src}: ${e.message}`)
    process.exitCode = 1
  }
}

const mb = (n) => (n / 1024 / 1024).toFixed(2)
console.log(
  `[to-webp] ${targets.length} imagem(ns): ${mb(before)}MB → ${mb(after)}MB ` +
    `(-${before ? (100 * (1 - after / before)).toFixed(0) : 0}%)`
)
