import React from 'react';
import { Scale, Cpu, Sparkles } from 'lucide-react';
import { PRESETS } from '../data/presets';

export default function Header({ isBackendOnline, selectedPreset, onSelectPreset }) {
  return (
    <header className="app-header">
      <div className="header-brand">
        <div className="logo-badge">
          <Scale size={22} />
        </div>
        <div>
          <div className="brand-title">MotionForge AI</div>
          <div className="brand-sub">Legal Draft & Motion Generator Agent</div>
        </div>
      </div>

      <div className="header-actions">
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Sparkles size={16} style={{ color: '#38bdf8' }} />
          <select 
            value={selectedPreset} 
            onChange={(e) => onSelectPreset(e.target.value)}
            style={{
              background: '#1e293b',
              color: '#f8fafc',
              border: '1px solid #334155',
              padding: '6px 12px',
              borderRadius: '8px',
              fontSize: '0.85rem',
              outline: 'none',
              cursor: 'pointer'
            }}
          >
            {PRESETS.map((p) => (
              <option key={p.id} value={p.id}>
                Preset: {p.name}
              </option>
            ))}
          </select>
        </div>

        <div className="status-badge">
          <div className="status-dot"></div>
          <span>FastAPI {isBackendOnline ? 'Online (Port 8000)' : 'Connected'}</span>
        </div>
      </div>
    </header>
  );
}
