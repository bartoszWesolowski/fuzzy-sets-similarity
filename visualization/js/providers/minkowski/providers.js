window.MinkowskiProvider = window.MinkowskiProvider || {};

window.MinkowskiProvider.method = 'minkowski';

window.MinkowskiProvider.buttonSelector = '.minkowski-calculate-button';

window.MinkowskiProvider.configExtractor = ($configDiv) => {
    let rValue = $configDiv.find('.config-r').val();
    return {
        r: parseInt(rValue) || 2
    };
}
