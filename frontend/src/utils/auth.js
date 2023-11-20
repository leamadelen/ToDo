import store from '../store';

export function getToken() {
    const token = localStorage.getItem('token');
    if (!token) {
      store.dispatch('logout'); 
      return null; 
    }
    
    const tokenData = JSON.parse(atob(token.split('.')[1])); 
    const expirationDate = new Date(tokenData.exp * 1000); 
  
    // Checking if the token has expired
    if (expirationDate <= new Date()) {
      localStorage.removeItem('token'); 
      store.dispatch('logout'); 
      return null; 
    }
  
    store.dispatch('login'); 
    return token; 
}