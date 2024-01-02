import React from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '../public/vite.svg'
import './App.css'

function App (): React.ReactNode {
  const [count, setCount] = React.useState(0)

  return (
    <div>
      <div>
        <a href='https://vitejs.dev' target='_blank' rel="noreferrer">
          <img src={viteLogo} className='logo' alt='Vite logo' />
        </a>
        <a href='https://react.dev' target='_blank' rel="noreferrer">
          <img src={reactLogo} className='logo react' alt='React logo' />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className='card'>
        <button onClick={() => { setCount((count) => count + 1) }}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className='read-the-docs'>
        Click on the Vite and React logos to learn more
      </p>
    </div>
  )
}

export default App