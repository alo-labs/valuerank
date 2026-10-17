// Recording stand-in for the Plotly global. Every call is appended to `calls`
// and returns a promise, like the real library.
export function createFakePlotly({ failOn } = {}) {
  const calls = [];
  const record = (method) => (...args) => {
    calls.push({ method, args });
    return failOn === method ? Promise.reject(new Error(`${method} failed`)) : Promise.resolve(args[0]);
  };
  return {
    calls,
    newPlot: record('newPlot'),
    react: record('react'),
    relayout: record('relayout'),
    restyle: record('restyle'),
    of: (method) => calls.filter((call) => call.method === method),
  };
}
