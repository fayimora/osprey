import React from 'react';
import axios from 'axios';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      torrents: []
    };
  }

  componentDidMount() {
    this.search('designated');
  }

  search = (searchTerm) => {
    axios.get(`http://localhost:8090/search/${searchTerm}`)
      .then(res => {
        this.setState({
          torrents: res.data
        });
      });
  }

  render () {
    const torrents = this.state.torrents;
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

        <h2>My Data</h2>
        <div className="container">
          <ul>
            {torrents.map(torrent =>
              <li key={torrent.id}>{torrent.name}</li>
            )}
          </ul>
        </div>

        <footer className="footer">
          <p>&copy; 2017 Fayimora</p>
        </footer>
      </div>
    );
  }
}

export default App;
