window.JaccardIndexProvider = window.JaccardIndexProvider || {};

window.JaccardIndexProvider.method = 'jaccard_index';

window.JaccardIndexProvider.buttonSelector = '.jaccard-index-calculate-button';

window.JaccardIndexProvider.configExtractor = ($configDiv) => {
    let alpha = $configDiv.find('.config-alpha').val();
    let beta = $configDiv.find('.config-beta').val();
    let gamma = $configDiv.find('.config-gamma').val();
    return {
        alpha: parseInt(alpha) || 1,
        beta: parseInt(beta) || 1,
        gamma: parseInt(gamma) || 1,
        evaluator: 'sup'
    };
}
