import React from 'react';
import axios from 'axios';
import config from '../../config/environment';

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

  handleEnter = (e) => {
    if(e.key==='Enter'){
      const searchTerm = e.target.value;
      this.search(searchTerm);
    }
  }

  search = (searchTerm) => {
    const url = `${config.API_URL}/search/${searchTerm}`;
    axios.get(url)
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

        <input
          type="text"
          className="form-control"
          id="searchField"
          placeholder="The Flash s02e03"
          onKeyPress={this.handleEnter}
        />

        <h2>My Data</h2>
        <div className="container">
          <table className="table table-striped">
            <thead>
              <tr>
                <td>Name</td>
              </tr>
            </thead>
            <tbody>
              {torrents.map(torrent =>
                <tr key={torrent.id}>
                  <td><a target="_blank" href={torrent.url}>{torrent.name}</a></td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        <footer className="footer">
          <p>&copy; 2017 Fayimora</p>
        </footer>
      </div>
    );
  }
}

export default App;
