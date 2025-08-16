import React, { useState } from "react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import "./App.css";

const inputTextAreaInlineStyles = {
  width: "100%",
  padding: "10px",
  fontSize: "16px",
  border: "1px solid #ccc",
  borderRadius: "4px",
  boxSizing: "border-box",
};

function App() {
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async () => {
    console.log("Button clicked, sending request to server...");
    setIsLoading(true);
    const currentuserInput = userInput.trim();
    setMessages([...messages, currentuserInput]);
    try {
      const response = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: userInput,
        }),
      });

      const data = await response.json();
      console.log("Response from server:", data);
      setMessages((prevMessages) => [...prevMessages, data.gemini_response]);
      setUserInput("");
      setIsLoading(false);
    } catch (error) {
      console.error("Error during fetch:", error);
    }
  };

  const Loader = <p>Loading...</p>;

  return (
    <>
      <h1 className="welcome-heading">Welcome to Guardian A11Y !</h1>

      <div>
        messages:
        {messages.length > 0 ? (
          messages.map((input, index) => (
             <Markdown key={index} remarkPlugins={[remarkGfm]}>
            {input.toString()}
          </Markdown>
          ))
        ) : (
          <p>No user inputs yet.</p>
          )}
      </div>

      {/* {isLoading ? (
        Loader
      ) : (
        <div
          style={{ background: "gray", padding: "20px", borderRadius: "8px" }}
        >
          <Markdown remarkPlugins={[remarkGfm]}>
            {accces_data.toString()}
          </Markdown>
        </div>
      )} */}

      <input
        type="text"
        value={userInput}
        placeholder="Feed the snippet"
        aria-label="Name input field"
        style={inputTextAreaInlineStyles}
        onChange={(e) => setUserInput(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
}

export default App;
