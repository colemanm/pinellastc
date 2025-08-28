export default function handler(req, res) {
  // Set CORS headers for client-side access
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Only allow GET requests
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  // Return environment variables that are safe to expose to the client
  res.status(200).json({
    MAPBOX_ACCESS_TOKEN: process.env.MAPBOX_ACCESS_TOKEN || ''
  });
}
