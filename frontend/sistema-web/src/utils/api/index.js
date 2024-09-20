const API_BASE_URL = 'http://localhost:5000'; // URL del backend

export async function fetchFireData(region) {
  const response = await fetch(`${API_BASE_URL}/fires/${region}`);
  if (!response.ok) {
    throw new Error('Error al obtener datos de incendios');
  }
  return response.json();
}
