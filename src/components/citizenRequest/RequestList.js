import React, { useEffect, useState } from "react";
import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { connect } from "react-redux";
import { get_citizenRequests } from "redux/actions/citizenRequests/citizenRequests";
import RequestElement from "./RequestElement";
import LoadingIcon from "components/LoadingIcon";

function RequestList({ get_citizenRequests, citizenRequests }) {
  const [loading, setLoading] = useState(true); 

  useEffect(() => {
    window.scrollTo(0, 0);
    get_citizenRequests().finally(() => setLoading(false)); 
  }, [get_citizenRequests]);

  console.log('citizenRequests: ', citizenRequests);

  const renderContent = () => {
    if (loading) {
      return <LoadingIcon />;
    }

    if (!citizenRequests || !citizenRequests.results.length) {
      return <p>No se encontraron solicitudes.</p>;
    }

    return (
      <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">Folio</th>
              <th scope="col" className="px-6 py-3">Tipo solicitud</th>
              <th scope="col" className="px-6 py-3">Area</th>
              <th scope="col" className="px-6 py-3">Fecha recepción</th>
              <th scope="col" className="px-6 py-3">Fecha máxima de respuesta</th>
              <th scope="col" className="px-6 py-3">Estado</th>
            </tr>
          </thead>
          <tbody>
            {citizenRequests.results.map((request, index) => (
              <RequestElement key={request.id} request={request} index={index} />
            ))}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <Layout>
      <Navbar />
      <div className="max-w-4xl mx-auto mt-8 text-white">
        <h1 className="text-2xl font-bold mb-4">Lista de Solicitudes OIRS</h1>
        {renderContent()}
      </div>
      <Footer />
    </Layout>
  );
}

const mapStateToProps = (state) => ({
  citizenRequests: state.citizenRequests.citizenRequests,
});

export default connect(mapStateToProps, { get_citizenRequests })(RequestList);
