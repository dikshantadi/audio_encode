import './App.css';

const Hello = () => {
  return (
    <div>
      <p> Hello World </p>
    </div>
  )
}
function App() {
  return (
    <div className="App">
      <h1> Greetings </h1>
      <Hello />
    </div>
  );
}

export default App;
