(() => {
  const form = document.querySelector('.subscribe-form');
  if (!form) return;
  const input = form.querySelector('[type="email"]');
  const submit = form.querySelector('button');
  const status = form.querySelector('[role="status"]');
  const live = ['https://vibegraph.md', 'https://www.vibegraph.md'].includes(location.origin);
  let busy = false;
  status.textContent = live ? form.dataset.liveNotice : form.dataset.previewNotice;
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (busy) return;
    input.setAttribute('aria-invalid', String(!input.validity.valid));
    if (!input.validity.valid) {
      form.dataset.state = 'error';
      status.textContent = form.dataset.invalidEmail;
      input.focus();
      return;
    }
    if (!live) {
      form.dataset.state = 'preview';
      status.textContent = form.dataset.previewResult;
      return;
    }
    busy = true;
    submit.disabled = true;
    form.setAttribute('aria-busy', 'true');
    form.dataset.state = 'pending';
    status.textContent = form.dataset.pending;
    try {
      const response = await fetch('https://vibegraph.ai/api/subscribe/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: input.value.trim(), website: form.querySelector('[name="website"]').value }),
        signal: AbortSignal.timeout(12000),
      });
      const result = await response.json();
      if (!response.ok || result.code !== 'received') throw new Error('Unavailable');
      form.dataset.state = 'success';
      status.textContent = form.dataset.received;
      input.value = '';
    } catch {
      form.dataset.state = 'error';
      status.textContent = form.dataset.unavailable;
    } finally {
      busy = false;
      submit.disabled = false;
      form.removeAttribute('aria-busy');
    }
  });
  input.disabled = false;
  submit.disabled = false;
})();
