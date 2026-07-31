const API_BASE = '/api';

export async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    return await res.json();
  } catch (err) {
    console.warn('Backend health check failed, utilizing fallback mode', err);
    return { status: 'offline' };
  }
}

export async function uploadFormatDocument(fileOrText) {
  try {
    const formData = new FormData();
    if (typeof fileOrText === 'string') {
      formData.append('text_content', fileOrText);
    } else {
      formData.append('file', fileOrText);
    }
    const res = await fetch(`${API_BASE}/upload-format`, {
      method: 'POST',
      body: formData
    });
    return await res.json();
  } catch (err) {
    console.error('Error uploading format:', err);
    throw err;
  }
}

export async function uploadReferenceDocument(fileOrText) {
  try {
    const formData = new FormData();
    if (typeof fileOrText === 'string') {
      formData.append('text_content', fileOrText);
    } else {
      formData.append('file', fileOrText);
    }
    const res = await fetch(`${API_BASE}/upload-reference`, {
      method: 'POST',
      body: formData
    });
    return await res.json();
  } catch (err) {
    console.error('Error uploading reference:', err);
    throw err;
  }
}

export async function generateMotionPipeline(formatText, referenceText, presetId = 'preset_frcp_37') {
  try {
    const res = await fetch(`${API_BASE}/generate-motion`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        format_text: formatText,
        reference_text: referenceText,
        preset_id: presetId,
        include_web_search: true
      })
    });
    return await res.json();
  } catch (err) {
    console.error('Error executing motion pipeline:', err);
    throw err;
  }
}
