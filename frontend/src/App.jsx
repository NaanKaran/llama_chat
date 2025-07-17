import { useState } from 'react'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const apiUrl = import.meta.env.VITE_API_URL || ''

  const sendMessage = async () => {
    const text = input.trim()
    if (!text) return
    const userMsg = { role: 'user', content: text }
    setMessages((m) => [...m, userMsg])
    setInput('')
    try {
      const res = await fetch(`${apiUrl}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      })
      const data = await res.json()
      setMessages((m) => [...m, { role: 'assistant', content: data.response }])
    } catch (err) {
      setMessages((m) => [
        ...m,
        { role: 'assistant', content: 'Error: ' + err.message }
      ])
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((m, i) => (
          <div key={i} className={`message ${m.role === 'user' ? 'user' : 'bot'}`}>{m.content}</div>
        ))}
      </div>
      <div className="input-area">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          rows={2}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  )
}

export default App
