import React from 'react';

class App extends React.Component {
  render () {
    return (
      <div className="container">
        <div className="header clearfix">
          <nav>
            <ul className="nav nav-pills pull-right">
              <li> <a href="#">Home</a> </li>
              <li> <a href="#">About</a> </li>
            </ul>
          </nav>
          <h3 className="text-muted">Osprey</h3>
        </div>

        <div className="jumbotron">
          <h1>Welcome to Osprey!!!</h1>
        </div>

        <footer className="footer">
          <p>&copy; 2016 Fayimora</p>
        </footer>
      </div>
    );
  }
}

export default App;
