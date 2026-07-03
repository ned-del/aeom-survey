import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the form submit handler with one that posts to Apps Script
old_script = """document.getElementById('surveyForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Collect form data
  const formData = new FormData(this);
  const data = {};
  for (let [key, value] of formData.entries()) {
    if (data[key]) {
      if (Array.isArray(data[key])) data[key].push(value);
      else data[key] = [data[key], value];
    } else {
      data[key] = value;
    }
  }
  
  console.log('Survey response:', data);
  
  // TODO: Replace with actual form submission endpoint
  // fetch('YOUR_ENDPOINT', { method: 'POST', body: JSON.stringify(data) });
  
  // Show thank you
  document.querySelector('.hero').style.display = 'none';
  document.querySelector('.letter-section').style.display = 'none';
  document.querySelector('.divider').style.display = 'none';
  document.querySelector('.survey-section').style.display = 'none';
  document.getElementById('thankYou').classList.add('show');
  window.scrollTo(0, 0);
});"""

new_script = """document.getElementById('surveyForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  
  const btn = document.querySelector('.submit-btn');
  btn.textContent = 'Sending...';
  btn.disabled = true;
  
  const formData = new FormData(this);
  const data = {};
  for (let [key, value] of formData.entries()) {
    if (data[key]) {
      if (Array.isArray(data[key])) data[key].push(value);
      else data[key] = [data[key], value];
    } else {
      data[key] = value;
    }
  }
  
  // Submit to Google Apps Script
  const ENDPOINT = 'APPS_SCRIPT_URL';
  try {
    if (ENDPOINT !== 'APPS_SCRIPT_URL') {
      await fetch(ENDPOINT, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
    }
  } catch(err) {
    console.log('Submission note:', err);
  }
  
  // Show thank you
  document.querySelector('.hero').style.display = 'none';
  document.querySelector('.letter-section').style.display = 'none';
  document.querySelector('.divider').style.display = 'none';
  document.querySelector('.survey-section').style.display = 'none';
  document.getElementById('thankYou').classList.add('show');
  window.scrollTo(0, 0);
});"""

html = html.replace(old_script, new_script)

with open('index.html', 'w') as f:
    f.write(html)

print("Updated")
