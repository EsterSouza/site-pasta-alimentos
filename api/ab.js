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

  const target = variant === 'b' ? '/b/index.html' : '/index.html';
  const origin = new URL(target, url.origin);
  const response = await fetch(origin);

  const newResponse = new Response(response.body, {
    status: response.status,
    headers: response.headers,
  });

  if (!match) {
    newResponse.headers.append(
      'Set-Cookie',
      `${COOKIE}=${variant}; Path=/; Max-Age=${30 * 24 * 60 * 60}; SameSite=Lax`
    );
  }

  return newResponse;
}
