import React, { useState, useRef, useEffect } from 'react';
import './LinedTextArea.css';

function LinedTextArea({ value, onChange }) {
  const [lineNumbers, setLineNumbers] = useState([]);
  const textAreaRef = useRef(null);

  const handleScroll = () => {
    const textArea = textAreaRef.current;
    const scrollTop = textArea.scrollTop;
    const lineNumberDiv = document.getElementById('line-numbers');
    lineNumberDiv.scrollTop = scrollTop;
  };

  useEffect(() => {
    const lines = value.split('\n').map((_, index) => index + 1);
    setLineNumbers(lines);
  }, [value]);

  return (
    <div className="lined-text-area">
      <div id="line-numbers" className="line-numbers">
        {lineNumbers.map((number) => (
          <div key={number}>{number}</div>
        ))}
      </div>
      <textarea
        ref={textAreaRef}
        value={value}
        onChange={onChange}
        onScroll={handleScroll}
        className="text-area"
        spellCheck="false"
      />
    </div>
  );
}

export default LinedTextArea;
