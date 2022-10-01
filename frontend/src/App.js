import './App.css';
import InputComponent from './components/InputComponent';
import mainLogo from './free-icon-nuevo-sol-3154126.png';

function App() {

  return (
    <>
      <img className="logo" src={mainLogo} alt="logo" />
      <div className="container">
        <InputComponent />
      </div>
    </>
  );
}

export default App;
