import "./styles/App.scss";
import { Switch, Route } from "react-router-dom";

import Header from "./navigation/Header";
import Footer from "./navigation/Footer";
import DefaultContainer from "./routing/DefaultContainer";
import LandingPage from "./pages/LandingPage";

function App() {
  return (
    <div className="App">
      <Header />

      <Switch>
        <Route component={DefaultContainer} />
        <Route exact path="/" component={LandingPage} />
      </Switch>

      <Footer />
    </div>
  );
}

export default App;
