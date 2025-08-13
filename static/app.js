async function predict(event) {
  event.preventDefault();
  const submitButton = event.target.querySelector('button[type="submit"]');
  submitButton.disabled = true;
  submitButton.textContent = 'Predicting...';

  const payload = {
    sepal_length: parseFloat(document.getElementById('sepal_length').value),
    sepal_width: parseFloat(document.getElementById('sepal_width').value),
    petal_length: parseFloat(document.getElementById('petal_length').value),
    petal_width: parseFloat(document.getElementById('petal_width').value),
  };

  try {
    const res = await fetch('/api/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(errText || 'Request failed');
    }

    const data = await res.json();
    document.getElementById('result').classList.remove('hidden');
    document.getElementById('predicted_class').textContent = data.predicted_class;

    const probsEl = document.getElementById('probabilities');
    probsEl.innerHTML = '';
    const entries = Object.entries(data.probabilities)
      .sort((a, b) => b[1] - a[1])
      .map(([k, v]) => `${k}: ${(v * 100).toFixed(1)}%`)
      .join('<br/>');
    probsEl.innerHTML = entries;
  } catch (err) {
    alert(`Error: ${err.message}`);
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = 'Predict';
  }
}

const form = document.getElementById('predict-form');
form.addEventListener('submit', predict);