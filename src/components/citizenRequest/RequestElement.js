import React, { useState } from "react";

function RequestElement({ request, index }) {
  const [openAccordion, setOpenAccordion] = useState(null);

  const toggleAccordion = (index) => {
    setOpenAccordion(openAccordion === index ? null : index);
  };

  return (
    <React.Fragment key={request.id}>
      <tr
        onClick={() => toggleAccordion(index)}
        className="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 cursor-pointer"
      >
        <td className="px-6 py-4">{request.folio}</td>
        <td className="px-6 py-4">{request.tipo_solicitud?.nombre}</td>
        <td className="px-6 py-4">{request.area?.nombre}</td>
        <td className="px-6 py-4">
          {new Date(request.fecha_recepcion).toLocaleDateString()}
        </td>
        <td className="px-6 py-4">
          {new Date(request.fecha_maxima_respuesta).toLocaleDateString()}
        </td>
        <td className="px-6 py-4">{request.estado_respuesta?.nombre}</td>
      </tr>
      {openAccordion === index && (
        <tr>
          <td colSpan="6" className="bg-gray-50 dark:bg-gray-900 p-4">
            {/* Flex container to divide into two columns */}
            <div className="flex justify-between space-x-4">
              {/* Left Column - Main Information */}
              <div className="w-1/2 text-gray-500 dark:text-gray-400 space-y-2">
                <p>
                  <strong>Nombre usuario:</strong>{" "}
                  {request.nombre_usuario}
                </p>
                <p>
                  <strong>Rut usuario:</strong>{" "}
                  {request.rut_usuario}
                </p>
                <p>
                  <strong>Texto de Solicitud:</strong> {request.texto_solicitud}
                </p>
              </div>

              {/* Right Column - Seguimiento de la Solicitud */}

              <ol class="relative border-s border-gray-200 dark:border-gray-700">
                <li class="mb-10 ms-4">
                  <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                  <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                    {new Date(request.fecha_recepcion).toLocaleDateString()}
                  </time>
                  <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                    Recepción de solicitud
                  </h3>
                  <p>
                    <strong>Vía de ingreso: </strong>{" "}
                    {request.via_ingreso?.nombre}
                  </p>
                  <p>
                    <strong>Fecha Máxima de Respuesta:</strong>{" "}
                    {new Date(
                      request.fecha_maxima_respuesta
                    ).toLocaleDateString()}
                  </p>
                  
                </li>
                <li class="mb-10 ms-4">
                  <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                  <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                    {new Date(
                      request.fecha_envio_funcionario
                    ).toLocaleDateString()}
                  </time>
                  <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                    Envío al funcionario
                  </h3>
                  <p class="text-base font-normal text-gray-500 dark:text-gray-400">
                    Funcionario aludido: {request.funcionario_aludido}
                  </p>
                  <p class="text-base font-normal text-gray-500 dark:text-gray-400">
                    Sector: {request.sector.nombre}
                  </p>
                </li>
                <li class="mb-10 ms-4">
                  <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                  <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                    {request.fecha_recepcion_descargo
                      ? new Date(
                          request.fecha_recepcion_descargo
                        ).toLocaleDateString()
                      : "No disponible"}
                  </time>
                  <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                    Recepción descargo de funcionario
                  </h3>
                </li>
                <li class="ms-4">
                  <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -start-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
                  <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">
                    {request.fecha_respuesta_entregada
                      ? new Date(
                          request.fecha_respuesta_entregada
                        ).toLocaleDateString()
                      : "No disponible"}
                  </time>
                  <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                    Envío de respuesta
                  </h3>
                </li>
              </ol>
            </div>

            {/* Action Buttons */}
            <div className="flex space-x-4 mt-4">
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
  );
}

export default RequestElement;
