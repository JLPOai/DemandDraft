import React, { useRef } from 'react';
import { Upload, FileText, CheckCircle, FileCode, Layers, ShieldCheck } from 'lucide-react';

export default function DocumentUploadSection({
  formatText,
  setFormatText,
  refText,
  setRefText,
  formatAnalysis,
  caseFacts,
  isProcessing,
  onRunPipeline
}) {
  const formatInputRef = useRef(null);
  const refInputRef = useRef(null);

  const handleFormatFile = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      setFormatText(event.target.result);
    };
    reader.readAsText(file);
  };

  const handleRefFile = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      setRefText(event.target.result);
    };
    reader.readAsText(file);
  };

  return (
    <div className="sidebar-panel">
      {/* Upload 1: Client Guideline & Format Document */}
      <div className="glass-card">
        <div className="card-title-row">
          <div className="card-title">
            <Layers size={18} />
            <span>1. Format & Guideline Template</span>
          </div>
          <span style={{ fontSize: '0.75rem', color: '#64748b' }}>Client Document</span>
        </div>

        <div 
          className="upload-dropzone" 
          onClick={() => formatInputRef.current?.click()}
        >
          <input 
            type="file" 
            ref={formatInputRef} 
            onChange={handleFormatFile} 
            style={{ display: 'none' }} 
            accept=".txt,.md,.doc,.docx,.pdf"
          />
          <div className="dropzone-icon">
            <Upload size={20} />
          </div>
          <div className="dropzone-text">Upload Client Format Sample</div>
          <div className="dropzone-sub">Target layout, caption & header rules</div>
        </div>

        <textarea
          value={formatText}
          onChange={(e) => setFormatText(e.target.value)}
          placeholder="Paste or view template format text..."
          rows={5}
          style={{
            width: '100%',
            marginTop: '12px',
            background: 'rgba(15, 23, 42, 0.6)',
            border: '1px solid #233152',
            borderRadius: '8px',
            color: '#cbd5e1',
            padding: '10px',
            fontSize: '0.8rem',
            fontFamily: 'JetBrains Mono, monospace',
            resize: 'vertical'
          }}
        />

        {formatAnalysis && (
          <div style={{ marginTop: '10px', padding: '8px 12px', background: 'rgba(59, 130, 246, 0.1)', borderRadius: '8px', border: '1px solid rgba(59, 130, 246, 0.3)' }}>
            <div style={{ fontSize: '0.75rem', fontWeight: '600', color: '#93c5fd', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <ShieldCheck size={14} /> Learned Format Guidelines
            </div>
            <div style={{ fontSize: '0.7rem', color: '#cbd5e1', marginTop: '4px' }}>
              • Caption: {formatAnalysis.caption_structure}<br />
              • Sections: {formatAnalysis.sections?.slice(0, 3).join(', ')}...
            </div>
          </div>
        )}
      </div>

      {/* Upload 2: Reference Document */}
      <div className="glass-card">
        <div className="card-title-row">
          <div className="card-title">
            <FileText size={18} />
            <span>2. Case Reference Document</span>
          </div>
          <span style={{ fontSize: '0.75rem', color: '#64748b' }}>Dispute Facts</span>
        </div>

        <div 
          className="upload-dropzone"
          onClick={() => refInputRef.current?.click()}
        >
          <input 
            type="file" 
            ref={refInputRef} 
            onChange={handleRefFile} 
            style={{ display: 'none' }} 
            accept=".txt,.md,.doc,.docx,.pdf"
          />
          <div className="dropzone-icon" style={{ background: 'rgba(139, 92, 246, 0.1)', color: '#a78bfa' }}>
            <FileCode size={20} />
          </div>
          <div className="dropzone-text">Upload Reference Case File</div>
          <div className="dropzone-sub">Case parties, facts & interrogatory details</div>
        </div>

        <textarea
          value={refText}
          onChange={(e) => setRefText(e.target.value)}
          placeholder="Paste or view case facts text..."
          rows={5}
          style={{
            width: '100%',
            marginTop: '12px',
            background: 'rgba(15, 23, 42, 0.6)',
            border: '1px solid #233152',
            borderRadius: '8px',
            color: '#cbd5e1',
            padding: '10px',
            fontSize: '0.8rem',
            fontFamily: 'JetBrains Mono, monospace',
            resize: 'vertical'
          }}
        />

        {caseFacts && (
          <div style={{ marginTop: '10px', padding: '8px 12px', background: 'rgba(139, 92, 246, 0.1)', borderRadius: '8px', border: '1px solid rgba(139, 92, 246, 0.3)' }}>
            <div style={{ fontSize: '0.75rem', fontWeight: '600', color: '#c084fc', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <CheckCircle size={14} /> Extracted Case Facts
            </div>
            <div style={{ fontSize: '0.7rem', color: '#cbd5e1', marginTop: '4px' }}>
              • {caseFacts.plaintiff} v. {caseFacts.defendant}<br />
              • Items: {caseFacts.discovery_items?.join(', ')}
            </div>
          </div>
        )}
      </div>

      {/* Action Button */}
      <button 
        className="btn-primary" 
        onClick={onRunPipeline} 
        disabled={isProcessing}
      >
        {isProcessing ? 'Agent Pipeline Running...' : 'Generate Motion Draft'}
      </button>
    </div>
  );
}
