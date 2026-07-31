import React from 'react';
import { Globe, ExternalLink, Bookmark, ShieldCheck, Scale } from 'lucide-react';

export default function SearchSourcesBlock({ sources }) {
  if (!sources || sources.length === 0) {
    return (
      <div className="glass-card">
        <div className="card-title-row">
          <div className="card-title">
            <Globe size={18} style={{ color: '#06b6d4' }} />
            <span>Web Search & Legal Sources Layer</span>
          </div>
          <span style={{ fontSize: '0.75rem', color: '#64748b' }}>Layer 3 Output</span>
        </div>
        <div style={{ fontSize: '0.85rem', color: '#64748b', textAlign: 'center', padding: '20px' }}>
          Execute the agent pipeline to view live legal web search sources and statutory citations.
        </div>
      </div>
    );
  }

  return (
    <div className="glass-card">
      <div className="card-title-row">
        <div className="card-title">
          <Globe size={18} style={{ color: '#06b6d4' }} />
          <span>Web Search Sources Searched for Motion Draft</span>
        </div>
        <span style={{ fontSize: '0.75rem', color: '#38bdf8', fontWeight: '600', display: 'flex', alignItems: 'center', gap: '4px' }}>
          <ShieldCheck size={14} /> {sources.length} Verified Sources
        </span>
      </div>

      <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginBottom: '12px' }}>
        The Agent Layer 3 searched web & legal databases for relevant rules of civil procedure, statutory authority, and precedent case law incorporated into the draft.
      </div>

      <div className="sources-grid">
        {sources.map((src) => (
          <div key={src.id} className="source-card">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <span className="source-tag">
                <Bookmark size={12} />
                {src.rule_tag}
              </span>
              <span style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: '600' }}>
                {(src.relevance_score * 100).toFixed(0)}% Match
              </span>
            </div>

            <div className="source-title">{src.title}</div>

            <a 
              href={src.url} 
              target="_blank" 
              rel="noopener noreferrer" 
              className="source-domain"
            >
              <ExternalLink size={12} />
              {src.domain}
            </a>

            <div className="source-snippet">
              "{src.snippet}"
            </div>

            <div style={{ fontSize: '0.7rem', color: '#64748b', marginTop: 'auto', display: 'flex', alignItems: 'center', gap: '4px' }}>
              <Scale size={12} /> {src.source_type}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
