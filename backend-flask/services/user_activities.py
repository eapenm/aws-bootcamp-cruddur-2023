from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
class UserActivities:
  def run(user_handle):
      # XRay.....
      segment = xray_recorder.begin_segment('user_activities')
      model = {
        'errors': None,
        'data': None
      }

      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        print("else:")
        sql = db.template('users','show')
        results = db.query_object_json(sql,{'handle': user_handle})
        model['data'] = results
        # XRay.....
        dict = {
          "now": now.isoformat(),
          "results-size": len(model['data'])
        }
        subsegment = xray_recorder.begin_subsegment('mock_data')
        segment.put_metadata('key', dict, 'namespace')
      return model