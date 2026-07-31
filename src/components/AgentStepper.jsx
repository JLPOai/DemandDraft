import React, { useState } from 'react';
import { Activity, CheckCircle2, Loader2, ChevronDown, ChevronUp, Terminal } from 'lucide-react';

export default function AgentStepper({ steps, isProcessing }) {
  const [expandedStep, setExpandedStep] = useState(3); // Expand search step by default

  const toggleExpand = (id) => {
    setExpandedStep(expandedStep === id ? null : id);
  };

  return (
    <div className="glass-card">
      <div className="card-title-row">
        <div className="card-title">
          <Activity size={18} style={{ color: '#f59e0b' }} />
          <span>Agent Execution Stepper & Live Logs</span>
        </div>
        <span style={{ fontSize: '0.75rem', color: '#94a3b8', display: 'flex', alignItems: 'center', gap: '4px' }}>
          <Terminal size={14} /> 4-Layer Pipeline
        </span>
      </div>

      <div className="stepper-container">
        {steps.map((step) => {
          const isCompleted = step.status === 'completed';
          const isRunning = step.status === 'running';
          const isExpanded = expandedStep === step.id;

          return (
            <div 
              key={step.id} 
              className={`step-card ${isCompleted ? 'completed' : isRunning ? 'running' : ''}`}
            >
              <div className="step-icon">
                {isCompleted ? (
                  <CheckCircle2 size={18} />
                ) : isRunning ? (
                  <Loader2 size={18} />
                ) : (
                  <span style={{ fontSize: '0.8rem', fontWeight: 'bold' }}>{step.id}</span>
                )}
              </div>

              <div className="step-info">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span className="step-layer">{step.layer_name}</span>
                  <span style={{ fontSize: '0.7rem', color: '#64748b' }}>{step.timestamp}</span>
                </div>

                <div className="step-header">{step.title}</div>
                <div className="step-details">{step.details}</div>

                {step.thoughts && step.thoughts.length > 0 && (
                  <button 
                    onClick={() => toggleExpand(step.id)}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#38bdf8',
                      fontSize: '0.75rem',
                      marginTop: '6px',
                      cursor: 'pointer',
                      display: 'flex',
                      align-items: 'center',
                      gap: '4px',
                      padding: 0
                    }}
                  >
                    {isExpanded ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                    {isExpanded ? 'Hide Agent Thoughts' : `View ${step.thoughts.length} Agent Execution Logs`}
                  </button>
                )}

                {isExpanded && step.thoughts && (
                  <div className="step-thoughts">
                    {step.thoughts.map((thought, idx) => (
                      <div key={idx} style={{ display: 'flex', gap: '6px' }}>
                        <span style={{ color: '#34d399' }}>❯</span>
                        <span>{thought}</span>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
