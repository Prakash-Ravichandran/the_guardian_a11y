import React, { useState } from "react";
// import Markdown from "react-markdown";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";
import remarkGfm from "remark-gfm";
import sendImg from "./assets/send.svg";
import { ShimmerLoader } from "./components/loader.jsx";
import "./App.css";

function App() {
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async () => {
    console.log("Button clicked, sending request to server...");
    setIsLoading(() => true);
    const currentuserInput = userInput.trim();
    setMessages([...messages, { text: currentuserInput, sender: "user" }]);
    setUserInput("");
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
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: data.gemini_response, sender: "assistant" },
      ]);
      setIsLoading(() => false);
    } catch (error) {
      console.error("Error during fetch:", error);
    }
  };

  // const Loader = () => <p>Loading...</p>;

  const AssistantComponent = ({ msg, index }) => {
    return (
      <div className={"assistant"} key={`${index}-assistant`}>
        <ReactMarkdown
          remarkPlugins={[remarkGfm]}
          key={`$${index}-assistant`}
          components={{
            code({ className, children, ...rest }) {
              const match = /language-(\w+)/.exec(className || "");
              return match ? (
                <SyntaxHighlighter
                  PreTag="div"
                  language={match[1]}
                  style={vscDarkPlus}
                  {...rest}
                >
                  {children}
                </SyntaxHighlighter>
              ) : (
                <code {...rest} className={className}>
                  {children}
                </code>
              );
            },
          }}
        >
          {msg}
        </ReactMarkdown>
      </div>
    );
  };

  return (
    <>
      {/* <h1 className="welcome-heading">Guardian A11Y! A Web for All, by All.</h1> */}
      <h1 className="welcome-heading">
        The Guardian A11Y ! Building an Inclusive Web
      </h1>
      <div className="chat-container">
        <div className="chat-nested-container">
          <div className="messages">
            {messages.length > 0 &&
              messages.map((msg, index) =>
                msg.sender === "user" ? (
                  <div className={"user"} key={`user-${index}`}>
                    {msg.text}
                  </div>
                ) : (
                  <AssistantComponent
                    msg={msg.text}
                    index={index}
                    key={`assistant-${index}`}
                  />
                )
              )}
            {isLoading && <ShimmerLoader />}
          </div>
        </div>
        <div
          className="query-container"
          style={{ position: "sticky", bottom: 0, width: "100%" }}
        >
          <div className="query">
            <textarea
              value={userInput}
              name="user-input"
              placeholder="Ask Guardian A11Y..."
              aria-label="user-input"
              className="input-textarea"
              onChange={(e) => setUserInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  handleSubmit();
                }
              }}
            />

            <div className="send">
              <button onClick={handleSubmit} className="send-button">
                <img src={sendImg} alt="Send" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
