from tethys_sdk.base import TethysAppBase, url_map_maker


class Streamflowbangladesh(TethysAppBase):
    """
    Tethys app class for Streamflowbangladesh.
    """

    name = 'ECMWF Streamflow Prediction Tool - Bangladesh'
    index = 'streamflowbangladesh:home'
    icon = 'streamflowbangladesh/images/icon.gif'
    package = 'streamflowbangladesh'
    root_url = 'streamflowbangladesh'
    color = '#27ae60'
    description = ''
    tags = 'ECMWF Streamflow Prediction'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='streamflowbangladesh',
                controller='streamflowbangladesh.controllers.home'
            ),
        )

        return url_maps


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='streamflowbangladesh',
                controller='streamflowbangladesh.controllers.index'),
            UrlMap(
                name='chart',
                url='streamflowbangladesh/chart',
                controller='streamflowbangladesh.controllers.chart'),
            UrlMap(
                name='forecastpercent',
                url='streamflowbangladesh/forecastpercent',
                controller='streamflowbangladesh.controllers.forecastpercent'),
            UrlMap(
                name='getFeatures',
                url='streamflowbangladesh/api/getFeatures',
                controller='streamflowbangladesh.api.getFeatures'),
            UrlMap(
                name='getreturnPeriod',
                url='streamflowbangladesh/api/getreturnPeriod',
                controller='streamflowbangladesh.api.getreturnPeriod'),
            UrlMap(
                name='getHistoric',
                url='streamflowbangladesh/api/getHistoric',
                controller='streamflowbangladesh.api.getHistoric'),
            UrlMap(
                name='getFlowDurationCurve',
                url='streamflowbangladesh/api/getFlowDurationCurve',
                controller='streamflowbangladesh.api.getFlowDurationCurve'),
            UrlMap(
                name='getForecast',
                url='streamflowbangladesh/api/getForecast',
                controller='streamflowbangladesh.api.getForecast'),
            UrlMap(
                name='getForecastCSV',
                url='streamflowbangladesh/getForecastCSV',
                controller='streamflowbangladesh.controllers.getForecastCSV'),
            UrlMap(
                name='getHistoricCSV',
                url='streamflowbangladesh/getHistoricCSV',
                controller='streamflowbangladesh.controllers.getHistoricCSV'),
        )

        return url_maps
