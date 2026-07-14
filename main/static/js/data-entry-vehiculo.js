// Script para mostrar el nombre del archivo seleccionado y una previsualización de éxito
const fileInput = document.getElementById('de_image');
const labelContainer = document.querySelector('label[for="de_image"]');
const textContainer = labelContainer.querySelector('div.flex-col');

// Guardar el contenido original para restaurarlo si el usuario cancela
const originalContent = textContainer.innerHTML;

fileInput.addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (file) {
        textContainer.innerHTML = `<div class="flex flex-col items-center justify-center p-4">
                        <div class="w-12 h-12 rounded-full bg-green-100 flex items-center justify-center mb-3">
                            <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                        </div>
                        <p class="text-sm font-semibold text-slate-800 text-center truncate w-full max-w-[200px]">${file.name}</p>
                        <p class="text-xs text-slate-500 mt-1">Listo para procesar</p>
                    </div>
                `;
        labelContainer.classList.add('border-green-400', 'bg-green-50');
        labelContainer.classList.remove('border-slate-300', 'bg-slate-50', 'hover:border-blue-500');
    } else {
        textContainer.innerHTML = originalContent;
        labelContainer.classList.remove('border-green-400', 'bg-green-50');
        labelContainer.classList.add('border-slate-300', 'bg-slate-50', 'hover:border-blue-500');
    }
});

// Manejo básico de drag & drop visual
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    labelContainer.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
    labelContainer.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
    labelContainer.addEventListener(eventName, unhighlight, false);
});

function highlight(e) {
    labelContainer.classList.add('border-blue-500', 'bg-blue-50');
}

function unhighlight(e) {
    labelContainer.classList.remove('border-blue-500', 'bg-blue-50');
}

labelContainer.addEventListener('drop', handleDrop, false);
function handleDrop(e) {
    let dt = e.dataTransfer;
    let files = dt.files;
    fileInput.files = files;
    // Desencadenar manualmente el evento change
    fileInput.dispatchEvent(new Event('change'));
}