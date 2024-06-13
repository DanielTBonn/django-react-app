import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

import Content from './components/content';



// function fetchData() {
  
//   useEffect(() => {
//     fetch('http://127.0.0.1:8000/api/restaurants/')
//       .then(res => res.json())
//       .then(data => setData(data))
//       .catch(err => console.log(err));
//       console.log(data)
    
//   }, [data]);
// }
function App() {

  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/restaurants/')
      .then(res => res.json())
      .then(data => {
        console.log(data)
        setData(data)})
      .catch(err => console.log(err));
    
  }, []);

  // console.log('RESPONSE: \n', response)

  return (
    <div>
      <h1 className="text-3xl font-bold underline">Hello World</h1>
      <Content />
      <p>{ data && data.length ? data[0].fields.name : 'Loading...' }</p>
    </div>
  )
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header>
  //   </div>
  // );
}

export default App;
