import React, { useState } from "react";
import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";

function RequestList() {
  const [openAccordion, setOpenAccordion] = useState(null);
  const [selectedMonth, setSelectedMonth] = useState("");

  const requests = [
    {
      id: "001",
      name: "Juan Pérez",
      date: "2024-07-20",
      details: "Solicitud de información sobre el programa de salud mental.",
    },
    {
      id: "002",
      name: "María González",
      date: "2024-08-02",
      details: "Reclamo por la demora en la atención médica.",
    },
    // Puedes agregar más datos de prueba aquí
  ];

  const toggleAccordion = (index) => {
    setOpenAccordion(openAccordion === index ? null : index);
  };

  const handleMonthChange = (e) => {
    setSelectedMonth(e.target.value);
  };

  const filteredRequests = requests.filter((request) => {
    if (!selectedMonth) return true;
    return new Date(request.date).getMonth() + 1 === parseInt(selectedMonth);
  });

  return (
    <Layout>
      <Navbar />
      <div className="max-w-4xl mx-auto mt-8 text-white">
        <h1 className="text-2xl font-bold mb-4">Lista de Solicitudes OIRS</h1>

        <div className="mb-4">
          <label htmlFor="month" className="block text-sm font-medium text-gray-300">
            Filtrar por Mes
          </label>
          <select
            id="month"
            name="month"
            className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            value={selectedMonth}
            onChange={handleMonthChange}
          >
            <option value="">Todos los Meses</option>
            <option value="1">Enero</option>
            <option value="2">Febrero</option>
            <option value="3">Marzo</option>
            <option value="4">Abril</option>
            <option value="5">Mayo</option>
            <option value="6">Junio</option>
            <option value="7">Julio</option>
            <option value="8">Agosto</option>
            <option value="9">Septiembre</option>
            <option value="10">Octubre</option>
            <option value="11">Noviembre</option>
            <option value="12">Diciembre</option>
          </select>
        </div>

        <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
          <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
            <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" className="px-6 py-3">Folio</th>
                <th scope="col" className="px-6 py-3">Nombre usuario</th>
                <th scope="col" className="px-6 py-3">Fecha</th>
              </tr>
            </thead>
            <tbody>
              {filteredRequests.map((request, index) => (
                <React.Fragment key={request.id}>
                  <tr
                    onClick={() => toggleAccordion(index)}
                    className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 cursor-pointer"
                  >
                    <td className="px-6 py-4">{request.id}</td>
                    <td className="px-6 py-4">{request.name}</td>
                    <td className="px-6 py-4">{request.date}</td>
                  </tr>
                  {openAccordion === index && (
                    <tr>
                      <td colSpan="3" className="bg-gray-50 dark:bg-gray-900 p-4">
                        <p className="text-gray-500 dark:text-gray-400 mb-4">
                          {request.details}
                        </p>
                        <div className="flex space-x-4">
                          <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500">
                            Editar
                          </button>
                          <button className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500">
                            Obtener Reporte
                          </button>
                        </div>
                      </td>
                    </tr>
                  )}
                </React.Fragment>
              ))}
            </tbody>
          </table>
        </div>
      </div>
      <Footer />
    </Layout>
  );
}

export default RequestList;
