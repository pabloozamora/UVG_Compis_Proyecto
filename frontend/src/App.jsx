import { useState } from 'react'
import TextArea from './components'
import './App.css'

function App() {
  const [code, setCode] = useState('')
  const [output, setOutput] = useState('')

  const handleCode = (e) => {
    setCode(e.target.value)
  }

  const handleOutput = async () => {
    await fetch('/compile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.output) {
          setOutput(data.output
            .split('\n')
            .map((line, index) => <p key={index}>{line}</p>))
        } else {
          setOutput(<p>{data.error}</p>)
        }
      })
      .catch((error) => {
        console.error('Error:', error)
        setOutput(<p>Error al compilar el código.</p>)
      })
  }

  return (
    <>
      <div>
        <h1>CompiScript</h1>
        <TextArea value={code} onChange={handleCode} />
        <button onClick={handleOutput}>Compilar</button>
        <div className="output">{output}</div>
      </div>
    </>
  )
}

export default App
