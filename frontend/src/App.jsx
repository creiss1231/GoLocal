import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import { store } from './store/store';
import ProtectedRoute from './components/protectedRoute.jsx';
import Login from './components/login/login.jsx';
import Signup from './components/signup/signup.jsx';
import Home from './components/home/home.jsx';
import Posts from './components/posts/posts.jsx';
import UserProfile from './components/userprofile/userprofile.jsx';
import EditProfile from './components/userprofile/EditProfile.jsx'; 
import SearchResults from './components/searchresults/SearchResults.jsx';
import Company from './components/company/company.jsx';
function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/home" element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          } />
          <Route path="/posts" element={
            <ProtectedRoute>
              <Posts />
            </ProtectedRoute>
          } />
           <Route path="/company" element={
            <ProtectedRoute>
              <Company />
            </ProtectedRoute>
          } />
          <Route path="/profile" element={
            <ProtectedRoute>
              <UserProfile />
            </ProtectedRoute>
          } />
          <Route path="/profile/edit" element={
            <ProtectedRoute>
              <EditProfile />
            </ProtectedRoute>
          } />
          <Route path="/search" element={
            <ProtectedRoute>
              <SearchResults />
            </ProtectedRoute>
          } />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
