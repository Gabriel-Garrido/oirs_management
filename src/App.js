import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import store from 'store';
import { Provider } from 'react-redux';
import Error404 from 'containers/errors/Error404'
import Home from 'containers/pages/Home';
import CitizenRequest from 'containers/pages/CitizenRequest';
import RequestList from 'components/citizenRequest/RequestList';
import NewRequest from 'components/citizenRequest/NewRequest';

function App() {
  return (
    <Provider store={store} >
      <Router>
        <Routes>
          <Route path="*" element={<Error404 />} />
          <Route path="/" element={<Home />} />
          <Route path="/citizenRequest" element={<CitizenRequest />} />
          <Route path="/requestList" element={<RequestList />} />
          <Route path="/newRequest" element={<NewRequest />} />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
