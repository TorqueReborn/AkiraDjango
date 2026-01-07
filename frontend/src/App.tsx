import Nav from "./Nav/Nav";
import Spotlight from "./Pages/Home/Spotlight/Spotlight";
import Trending from "./Pages/Home/Trending/Trending";

const Login: React.FC = () => {
    return <>
        <Nav/>
        <Spotlight/>
        <Trending/>
    </>
}

export default Login;