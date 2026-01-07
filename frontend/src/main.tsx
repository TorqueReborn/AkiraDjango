import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Watch from './Pages/Watch/Watch.tsx'
import Details from "./Pages/Details/Details.tsx"
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App/>,
    errorElement: <div>404 Not Found</div>
  }, {
    path: '/:id',
    element: <Details/>
  }, {
    path: '/watch/:id/:episode',
    element: <Watch/>
  }
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router}/>
  </StrictMode>,
)
