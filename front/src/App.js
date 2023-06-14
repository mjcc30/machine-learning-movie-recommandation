import "./App.css";
import Cinema from "./cinema.svg";

function App() {
  return (
    <>
      <div className="round absolute top-[-40%] left-[-20%] z-0 h-[1000px] w-[1000px]"></div>
      <div className="round absolute bottom-[-40%] right-[-20%] z-0 h-[1000px] w-[1000px]"></div>
      <div id="container">
        <div className="flex items-center gap-4 mb-24">
          <img src={Cinema} alt="" className="w-12 shadow-lg " />
          <h1 className="text-3xl font-bold text-red-600">MyMovies</h1>
        </div>
        <input
          type="text"
          name="search"
          placeholder="Rechercher un film..."
          className="color-gray-500 rounded-full px-4 py-2 w-[300px] focus:outline-none focus:ring-2 focus:ring-red-600"
        />
        <div className="flex flex-wrap gap-6 justify-center items-center w-1/2 mt-6">
          <div className="w-[300px] h-[400px] bg-gray-200 rounded-lg shadow-lg ">
            <div className="w-full h-[250px] bg-gray-400 rounded-t-lg"></div>
            <div className="w-full h-auto bg-white rounded-b-lg p-4">
              <h2 className="text-2xl font-bold text-black">Titre du film</h2>
              <p className="text-gray-500 text-sm mt-2">Date de sortie</p>
              <p className="text-gray-500 text-sm">Note</p>
              <p className="text-gray-500 text-sm">Nombre de votes</p>
              <p className="text-gray-500 text-sm">Description</p>

              <div className="flex justify-center items-center">
                <button className="bg-red-600 text-white rounded-full px-4 py-2 mt-4">
                  Voir le film
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
