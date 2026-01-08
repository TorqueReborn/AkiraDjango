const Favorites = () => {
  const getFavorites = async () => {
    const response = await fetch('http://127.0.0.1:8000/favorites/', {credentials: "include"})
  }
  getFavorites();
  return (
    <div>Favorites</div>
  )
}

export default Favorites