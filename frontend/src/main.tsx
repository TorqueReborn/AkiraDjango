import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Watch from './Pages/Watch/Watch.tsx'
import Login from './Pages/Login/Login.tsx'
import Search from './Pages/Search/Search.tsx'
import Details from './Pages/Details/Details.tsx'
import SavedLogins from './Pages/SavedLogins/SavedLogins.tsx'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Favorites from './Pages/Favorites/Favorites.tsx'

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
  }, {
    path: '/login',
    element: <Login/>
  }, {
    path: '/search',
    element: <Search/>
  }, {
    path: '/saved-logins',
    element: <SavedLogins/>
  }, {
    path: '/favorites',
    element: <Favorites/>
  }
])

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router}/>
  </StrictMode>,
)
