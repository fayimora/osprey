const setupConfig = (environment) => {
  const ENV = {
    API_URL: 'http://localhost:8090'
  };

  if(environment==='development'){
    // ... add stuff to ENV
    ENV.API_URL = 'http://localhost:8090'
  }

  if(environment==='production'){
    // ... add stuff to ENV
    ENV.API_URL = 'https://fayi-osprey.herokuapp.com'
  }

  return ENV;
}

// export the resulting config
export default setupConfig(process.env.NODE_ENV);
