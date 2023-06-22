import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const API_URL =
    "https://api.themoviedb.org/3/movie/popular?api_key=cf2252886d6a21af83168fc669f0fc4c";
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json)
      .then((data) => setMovies(data.results));
    console.log(movies);
  }, []);

  return (
    <div className="App">
      <div className="search_nav">
        <div>
          <h1>Movies</h1>
        </div>
        <div>
          <form>
            <input />
            <button>Search</button>
          </form>
        </div>
      </div>
      <div className="movies"></div>
    </div>
  );
}

export default App;
