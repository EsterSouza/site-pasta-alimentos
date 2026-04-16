# Guia: Configurar múltiplas contas GitHub no mesmo PC

Documentação de como configuramos duas contas GitHub (Michel e Ester) na mesma máquina usando chaves SSH diferentes.

## Estrutura

```
~/.ssh/
├── config                  # Define os hosts e qual chave cada um usa
├── id_ed25519              # Chave do Michel (conta principal)
├── id_ed25519.pub
├── id_rsa_github2          # Chave da Ester (segunda conta)
└── id_rsa_github2.pub
```

---

## 1. Gerar chaves SSH (uma por conta)

Se ainda não tem as chaves:

```bash
# Conta principal (Michel)
ssh-keygen -t ed25519 -C "michel.caiafa@gmail.com" -f ~/.ssh/id_ed25519

# Segunda conta (Ester)
ssh-keygen -t rsa -b 4096 -C "esterposte@hotmail.com" -f ~/.ssh/id_rsa_github2
```

Depois, adicionar cada chave pública (`.pub`) na respectiva conta do GitHub:
**GitHub → Settings → SSH and GPG keys → New SSH key**

---

## 2. Configurar ~/.ssh/config

```
# Conta do Michel (padrão)
Host github.com-github
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes

# Conta da Ester
Host github.com-github2
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_github2
  IdentitiesOnly yes
```

O truque é o **Host**: `github.com-github` e `github.com-github2` são apelidos que apontam para o mesmo `github.com`, mas cada um usa uma chave diferente.

---

## 3. Configurar o remote do repositório

O remote precisa usar o Host correto conforme a conta dona do repo:

```bash
# Repo do Michel → usa github.com-github
git remote set-url origin git@github.com-github:MichelCF/nome-do-repo.git

# Repo da Ester → usa github.com-github2
git remote set-url origin git@github.com-github2:EsterSouza/nome-do-repo.git
```

Para verificar:

```bash
git remote -v
```

---

## 4. Fazer commits com o autor correto

O `~/.gitconfig` global tem o Michel como padrão. Para commitar como Ester, usar flags `-c` no commit:

```bash
git -c user.name="Ester" -c user.email="esterposte@hotmail.com" commit -m "mensagem"
```

Ou configurar localmente no repo da Ester (vale só para aquele repo):

```bash
cd /caminho/do/repo-da-ester
git config user.name "Ester"
git config user.email "esterposte@hotmail.com"
```

---

## 5. Testar a conexão

```bash
# Testar chave do Michel
ssh -T git@github.com-github

# Testar chave da Ester
ssh -T git@github.com-github2
```

Deve retornar algo como:
```
Hi EsterSouza! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## Resumo rápido

| Conta | Host SSH | Chave | Email |
|---|---|---|---|
| Michel | `github.com-github` | `~/.ssh/id_ed25519` | michel.caiafa@gmail.com |
| Ester | `github.com-github2` | `~/.ssh/id_rsa_github2` | esterposte@hotmail.com |

## Checklist para adicionar uma terceira conta

- [ ] Gerar nova chave SSH (`ssh-keygen -f ~/.ssh/id_nome`)
- [ ] Adicionar a chave pública no GitHub da nova conta
- [ ] Adicionar novo bloco `Host github.com-github3` no `~/.ssh/config`
- [ ] Usar o Host correto no remote do repo (`git remote set-url origin git@github.com-github3:...`)
- [ ] Configurar `user.name` e `user.email` no repo ou via flags `-c`
