// Example API utility for frontend to call backend endpoints
export async function agentAct(input) {
  const response = await fetch('/agent/act', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ input }),
  });
  return response.json();
}
