import NewRequest from "components/citizenRequest/NewRequest";
import RequestList from "components/citizenRequest/RequestList";
import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { useState } from "react";
import { Link } from "react-router-dom";


function CitizenRequest() {
    const [selectedTab, setSelectedTab] = useState("requestList");

    const handleTabChange = (tab) => {
      setSelectedTab(tab);
    };
  return (
    <Layout>
      <Navbar />
      <div className="bg-slate-900 p-4 flex flex-col min-h-screen pb-20 mb-10">
        {/* Dropdown para pantallas pequeñas */}
        <div className="sm:hidden fixed w-full z-20 top-16 start-0 h-fit">
          <select
            id="tabs"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            value={selectedTab}
            onChange={(e) => handleTabChange(e.target.value)}
          >
            <option value="requestList">Request List</option>
            <option value="newRequest">New Request</option>
          </select>
        </div>

        {/* Tabs para pantallas más grandes */}
        <ul className="hidden text-sm font-medium text-center text-gray-500 rounded-lg shadow sm:flex dark:divide-gray-700 dark:text-gray-400">
          <li className="w-full focus-within:z-10">
            <button
              className={`inline-block w-full p-4 ${
                selectedTab === "requestList"
                  ? "text-gray-900 bg-gray-100 dark:bg-gray-700 dark:text-white"
                  : "bg-white dark:bg-gray-800 dark:text-gray-400"
              } border-r border-gray-200 dark:border-gray-700 rounded-s-lg focus:ring-4 focus:ring-blue-300 focus:outline-none`}
              onClick={() => handleTabChange("requestList")}
            >
              Lista de solicitudes
            </button>
          </li>
          <li className="w-full focus-within:z-10">
            <button
              className={`inline-block w-full p-4 ${
                selectedTab === "newRequest"
                  ? "text-gray-900 bg-gray-100 dark:bg-gray-700 dark:text-white"
                  : "bg-white dark:bg-gray-800 dark:text-gray-400"
              } border-r border-gray-200 dark:border-gray-700 focus:ring-4 focus:ring-blue-300 focus:outline-none`}
              onClick={() => handleTabChange("newRequest")}
            >
              Nueva solicitud
            </button>
          </li>
        </ul>

        {/* Renderizado condicional basado en la pestaña seleccionada */}
        <div className="">
          {selectedTab === "requestList" && <RequestList />}
          {selectedTab === "newRequest" && <NewRequest />}
        </div>
      </div>

      <Footer />
    </Layout>
  );
}

export default CitizenRequest;
