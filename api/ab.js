export const config = { runtime: 'edge' };

const COOKIE = 'ab-variant';

export default async function handler(request) {
  const url = new URL(request.url);
  const cookies = request.headers.get('cookie') || '';
  const match = cookies.match(new RegExp(`${COOKIE}=([ab])`));
  let variant = match ? match[1] : null;

  if (!variant) {
    variant = Math.random() < 0.5 ? 'a' : 'b';
  }

  const target = variant === 'b' ? '/b/' : '/a/';
  const headers = new Headers({ Location: new URL(target, url.origin).toString() });

  if (!match) {
    headers.append(
      'Set-Cookie',
      `${COOKIE}=${variant}; Path=/; Max-Age=${30 * 24 * 60 * 60}; SameSite=Lax`
    );
  }

  return new Response(null, { status: 302, headers });
}
