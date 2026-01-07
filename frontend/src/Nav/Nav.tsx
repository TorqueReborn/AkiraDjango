import Button from "./components/Button"

const Nav = () => {
  return (
    <div className="flex items-center relative h-16">
      <div className="absolute right-10">
        <Button />
      </div>
    </div>
  )
}

export default Nav