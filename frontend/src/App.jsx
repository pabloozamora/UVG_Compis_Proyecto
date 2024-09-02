import { useState } from 'react'
import LinedTextArea from './components'
import './App.css'

function App() {
  const [code, setCode] = useState('')
  const [output, setOutput] = useState('')

  const handleCode = (e) => {
    setCode(e.target.value)
  }

  const handleOutput = async () => {
    await fetch('/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ code }),
    })
      .then((response) => {
        console.log(response); // Verifica la respuesta de la API
        return response.json(); // Asegúrate de retornar la promesa de json()
      })
      .then((data) => {
        if (data.result) {
          console.log(data.result); // Verifica los datos recibidos
          setOutput(data.result
            .map((line, index) => <p key={index}>{line}</p>))
        } else {
          setOutput(<p>{data.error}</p>)
        }
      })
      .catch((error) => {
        console.error('Error:', error)
        setOutput(<p>Error al analizar el código.</p>)
      })
  }

  return (
    <>
      <div>
        <h1 className='title'>CompiScript</h1>
        <LinedTextArea value={code} onChange={handleCode} />
        <button className="compileButton" onClick={handleOutput}>Compilar</button>
        <div className="output">{output}</div>
      </div>
    </>
  )
}

export default App
