import { useState, useEffect } from "react";
import "./App.css";

function App(): JSX.Element {
  const [displayText, setDisplayText] = useState<string>(
    "Do you want to see some cats?"
  );
  const [showButtons, setShowButtons] = useState<boolean>(true);
  const [catImageUrl, setCatImageUrl] = useState<string>("");

  const fetchCatImage = async (): Promise<void> => {
    try {
      const response = await fetch(
        "https://api.thecatapi.com/v1/images/search"
      );
      const data = await response.json();
      if (data && data.length > 0) {
        setCatImageUrl(data[0].url);
      }
    } catch (error) {
      console.error("Error fetching cat image:", error);
    }
  };

  const handleYesClick = (): void => {
    setDisplayText("ฅ^•ﻌ•^ฅ");
    setShowButtons(false);
  };

  const handleNoClick = (): void => {
    setDisplayText("You will see them anyway >:(");
    setShowButtons(false);
  };

  const handleMeoMeoClick = (): void => {
    fetchCatImage();
  };

  useEffect(() => {
    fetchCatImage();
  }, []);

  return (
    <>
      <div className="h-screen flex flex-col items-center justify-center">
        <h1 className="text-4xl mb-4 drop-shadow-lg">{displayText}</h1>
        <div className={`mb-4 ${showButtons ? "hidden" : "block"}`}>
          <div>
            <img
              src={catImageUrl}
              alt="Cat"
              className="w-80 h-80 object-cover"
            />
          </div>
          <button
            className="mt-4 bg-pink-500 hover:bg-pink-400 text-white font-bold px-4 border-b-4 border-pink-700 hover:border-pink-500 py-2 rounded"
            onClick={handleMeoMeoClick}
          >
            meo meo
          </button>
        </div>
        <div className={`mt-4 ${showButtons ? "block" : "hidden"}`}>
          <button
            className="bg-pink-500 hover:bg-pink-400 text-white font-bold py-2 px-4 border-b-4 border-pink-700 hover:border-pink-500 rounded"
            onClick={handleYesClick}
          >
            Yes
          </button>
          <button
            className="bg-pink-400 hover:bg-pink-300 text-white font-bold py-2 px-4 border-b-4 border-pink-500 hover:border-pink-500 rounded ml-3"
            onClick={handleNoClick}
          >
            No
          </button>
        </div>
      </div>
    </>
  );
}

export default App;
