window.ChartCanvasExtractor = (function($) {

    /**
     * Extract canvas from closest canvas with chart-canvas available under main similarity section. 
     * Used for finding chart canvas on pages showing similarity of many fuzzy sets using same method for displaying chart
     * for each pair of sets
     */
    extracRelativeCanvas = ($mainSection) => {
        return $mainSection.find('.chart-canvas')[0];
    }

    
    extractGlobalCanvas = ($mainSection) => {
        return $('#chart-canvas')[0];
    }

    return {
        extracRelativeCanvas,
        extractGlobalCanvas,
    }
})($);