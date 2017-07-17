window.ConfigProvider = window.ConfigProvider || {};

ConfigProvider.extractConfig = ($configDiv) => {
    let rValue = $configDiv.find('.config-r').val();
    return {
        r: parseInt(rValue) || 2
        }
}

window.MethodProvider = window.MethodProvider || {};

MethodProvider.getMethodName =  () => {
    return 'minkowski';
}