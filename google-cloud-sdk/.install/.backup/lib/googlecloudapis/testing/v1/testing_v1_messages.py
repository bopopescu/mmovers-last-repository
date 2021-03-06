"""Generated message classes for testing version v1.

Allows developers to run automated tests for their applications on Google
infrastructure.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages


package = 'testing'


class AndroidDevice(messages.Message):
  """A AndroidDevice object.

  Fields:
    androidModelId: A string attribute.
    androidVersionId: A string attribute.
    locale: A string attribute.
    orientation: A string attribute.
  """

  androidModelId = messages.StringField(1)
  androidVersionId = messages.StringField(2)
  locale = messages.StringField(3)
  orientation = messages.StringField(4)


class AndroidDeviceCatalog(messages.Message):
  """A AndroidDeviceCatalog object.

  Fields:
    models: A AndroidModel attribute.
    runtimeConfiguration: A AndroidRuntimeConfiguration attribute.
    versions: A AndroidVersion attribute.
  """

  models = messages.MessageField('AndroidModel', 1, repeated=True)
  runtimeConfiguration = messages.MessageField('AndroidRuntimeConfiguration', 2)
  versions = messages.MessageField('AndroidVersion', 3, repeated=True)


class AndroidInstrumentationTest(messages.Message):
  """A AndroidInstrumentationTest object.

  Fields:
    appApk: A FileReference attribute.
    appPackageId: A string attribute.
    testApk: A FileReference attribute.
    testPackageId: A string attribute.
    testRunnerClass: A string attribute.
    testTargets: A string attribute.
  """

  appApk = messages.MessageField('FileReference', 1)
  appPackageId = messages.StringField(2)
  testApk = messages.MessageField('FileReference', 3)
  testPackageId = messages.StringField(4)
  testRunnerClass = messages.StringField(5)
  testTargets = messages.StringField(6, repeated=True)


class AndroidMatrix(messages.Message):
  """A AndroidMatrix object.

  Fields:
    androidModelIds: A string attribute.
    androidVersionIds: A string attribute.
    locales: A string attribute.
    orientations: A string attribute.
  """

  androidModelIds = messages.StringField(1, repeated=True)
  androidVersionIds = messages.StringField(2, repeated=True)
  locales = messages.StringField(3, repeated=True)
  orientations = messages.StringField(4, repeated=True)


class AndroidModel(messages.Message):
  """A AndroidModel object.

  Enums:
    FormValueValuesEnum:

  Fields:
    brand: A string attribute.
    codename: A string attribute.
    form: A FormValueValuesEnum attribute.
    id: A string attribute.
    manufacturer: A string attribute.
    name: A string attribute.
    screenX: A integer attribute.
    screenY: A integer attribute.
    supportedVersionIds: A string attribute.
    tags: A string attribute.
  """

  class FormValueValuesEnum(messages.Enum):
    """FormValueValuesEnum enum type.

    Values:
      PHYSICAL: <no description>
      UNSPECIFIED: <no description>
      VIRTUAL: <no description>
    """
    PHYSICAL = 0
    UNSPECIFIED = 1
    VIRTUAL = 2

  brand = messages.StringField(1)
  codename = messages.StringField(2)
  form = messages.EnumField('FormValueValuesEnum', 3)
  id = messages.StringField(4)
  manufacturer = messages.StringField(5)
  name = messages.StringField(6)
  screenX = messages.IntegerField(7, variant=messages.Variant.INT32)
  screenY = messages.IntegerField(8, variant=messages.Variant.INT32)
  supportedVersionIds = messages.StringField(9, repeated=True)
  tags = messages.StringField(10, repeated=True)


class AndroidMonkeyTest(messages.Message):
  """A AndroidMonkeyTest object.

  Fields:
    appApk: A FileReference attribute.
    appPackageId: A string attribute.
    eventCount: A integer attribute.
    eventDelay: A string attribute.
    randomSeed: A integer attribute.
  """

  appApk = messages.MessageField('FileReference', 1)
  appPackageId = messages.StringField(2)
  eventCount = messages.IntegerField(3, variant=messages.Variant.INT32)
  eventDelay = messages.StringField(4)
  randomSeed = messages.IntegerField(5, variant=messages.Variant.INT32)


class AndroidRoboTest(messages.Message):
  """A AndroidRoboTest object.

  Fields:
    appApk: A FileReference attribute.
    appInitialActivity: A string attribute.
    appPackageId: A string attribute.
    bootstrapApk: A FileReference attribute.
    bootstrapPackageId: A string attribute.
    bootstrapRunnerClass: A string attribute.
    maxDepth: A integer attribute.
    maxSteps: A integer attribute.
    randomizeSteps: A boolean attribute.
  """

  appApk = messages.MessageField('FileReference', 1)
  appInitialActivity = messages.StringField(2)
  appPackageId = messages.StringField(3)
  bootstrapApk = messages.MessageField('FileReference', 4)
  bootstrapPackageId = messages.StringField(5)
  bootstrapRunnerClass = messages.StringField(6)
  maxDepth = messages.IntegerField(7, variant=messages.Variant.INT32)
  maxSteps = messages.IntegerField(8, variant=messages.Variant.INT32)
  randomizeSteps = messages.BooleanField(9)


class AndroidRuntimeConfiguration(messages.Message):
  """A AndroidRuntimeConfiguration object.

  Fields:
    locales: A Locale attribute.
    orientations: A Orientation attribute.
  """

  locales = messages.MessageField('Locale', 1, repeated=True)
  orientations = messages.MessageField('Orientation', 2, repeated=True)


class AndroidVersion(messages.Message):
  """A AndroidVersion object.

  Fields:
    apiLevel: A integer attribute.
    codeName: A string attribute.
    distribution: A Distribution attribute.
    id: A string attribute.
    releaseDate: A string attribute.
    tags: A string attribute.
    versionString: A string attribute.
  """

  apiLevel = messages.IntegerField(1, variant=messages.Variant.INT32)
  codeName = messages.StringField(2)
  distribution = messages.MessageField('Distribution', 3)
  id = messages.StringField(4)
  releaseDate = messages.StringField(5)
  tags = messages.StringField(6, repeated=True)
  versionString = messages.StringField(7)


class BlobstoreFile(messages.Message):
  """A BlobstoreFile object.

  Fields:
    blobId: A string attribute.
    md5Hash: A string attribute.
  """

  blobId = messages.StringField(1)
  md5Hash = messages.StringField(2)


class Browser(messages.Message):
  """A Browser object.

  Fields:
    androidCatalog: A AndroidDeviceCatalog attribute.
    id: A string attribute.
    linuxCatalog: A LinuxMachineCatalog attribute.
    name: A string attribute.
    release: A string attribute.
    versionString: A string attribute.
    windowsCatalog: A WindowsMachineCatalog attribute.
  """

  androidCatalog = messages.MessageField('AndroidDeviceCatalog', 1)
  id = messages.StringField(2)
  linuxCatalog = messages.MessageField('LinuxMachineCatalog', 3)
  name = messages.StringField(4)
  release = messages.StringField(5)
  versionString = messages.StringField(6)
  windowsCatalog = messages.MessageField('WindowsMachineCatalog', 7)


class CancelTestExecutionResponse(messages.Message):
  """A CancelTestExecutionResponse object.

  Enums:
    TestStateValueValuesEnum:

  Fields:
    testState: A TestStateValueValuesEnum attribute.
  """

  class TestStateValueValuesEnum(messages.Enum):
    """TestStateValueValuesEnum enum type.

    Values:
      CANCELLED: <no description>
      ERROR: <no description>
      FINISHED: <no description>
      INVALID: <no description>
      IN_PROGRESS: <no description>
      PENDING: <no description>
      QUEUED: <no description>
      RUNNING: <no description>
      UNSPECIFIED_TEST_STATE: <no description>
      UNSUPPORTED_ENVIRONMENT: <no description>
      VALIDATING: <no description>
    """
    CANCELLED = 0
    ERROR = 1
    FINISHED = 2
    INVALID = 3
    IN_PROGRESS = 4
    PENDING = 5
    QUEUED = 6
    RUNNING = 7
    UNSPECIFIED_TEST_STATE = 8
    UNSUPPORTED_ENVIRONMENT = 9
    VALIDATING = 10

  testState = messages.EnumField('TestStateValueValuesEnum', 1)


class CancelTestMatrixResponse(messages.Message):
  """A CancelTestMatrixResponse object.

  Enums:
    TestStateValueValuesEnum:

  Fields:
    testState: A TestStateValueValuesEnum attribute.
  """

  class TestStateValueValuesEnum(messages.Enum):
    """TestStateValueValuesEnum enum type.

    Values:
      CANCELLED: <no description>
      ERROR: <no description>
      FINISHED: <no description>
      INVALID: <no description>
      IN_PROGRESS: <no description>
      PENDING: <no description>
      QUEUED: <no description>
      RUNNING: <no description>
      UNSPECIFIED_TEST_STATE: <no description>
      UNSUPPORTED_ENVIRONMENT: <no description>
      VALIDATING: <no description>
    """
    CANCELLED = 0
    ERROR = 1
    FINISHED = 2
    INVALID = 3
    IN_PROGRESS = 4
    PENDING = 5
    QUEUED = 6
    RUNNING = 7
    UNSPECIFIED_TEST_STATE = 8
    UNSUPPORTED_ENVIRONMENT = 9
    VALIDATING = 10

  testState = messages.EnumField('TestStateValueValuesEnum', 1)


class ClientInfo(messages.Message):
  """A ClientInfo object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1)


class ConnectionInfo(messages.Message):
  """A ConnectionInfo object.

  Fields:
    adbPort: A integer attribute.
    ipAddress: A string attribute.
    sshPort: A integer attribute.
    vncPassword: A string attribute.
    vncPort: A integer attribute.
  """

  adbPort = messages.IntegerField(1, variant=messages.Variant.INT32)
  ipAddress = messages.StringField(2)
  sshPort = messages.IntegerField(3, variant=messages.Variant.INT32)
  vncPassword = messages.StringField(4)
  vncPort = messages.IntegerField(5, variant=messages.Variant.INT32)


class Device(messages.Message):
  """A Device object.

  Enums:
    StateValueValuesEnum:

  Fields:
    androidDevice: A AndroidDevice attribute.
    creationTime: A string attribute.
    deviceDetails: A DeviceDetails attribute.
    id: A string attribute.
    state: A StateValueValuesEnum attribute.
    stateDetails: A DeviceStateDetails attribute.
  """

  class StateValueValuesEnum(messages.Enum):
    """StateValueValuesEnum enum type.

    Values:
      CLOSED: <no description>
      DEVICE_ERROR: <no description>
      DEVICE_UNSPECIFIED: <no description>
      PREPARING: <no description>
      READY: <no description>
    """
    CLOSED = 0
    DEVICE_ERROR = 1
    DEVICE_UNSPECIFIED = 2
    PREPARING = 3
    READY = 4

  androidDevice = messages.MessageField('AndroidDevice', 1)
  creationTime = messages.StringField(2)
  deviceDetails = messages.MessageField('DeviceDetails', 3)
  id = messages.StringField(4)
  state = messages.EnumField('StateValueValuesEnum', 5)
  stateDetails = messages.MessageField('DeviceStateDetails', 6)


class DeviceDetails(messages.Message):
  """A DeviceDetails object.

  Fields:
    connectionInfo: A ConnectionInfo attribute.
    gceInstanceDetails: A GceInstanceDetails attribute.
  """

  connectionInfo = messages.MessageField('ConnectionInfo', 1)
  gceInstanceDetails = messages.MessageField('GceInstanceDetails', 2)


class DeviceStateDetails(messages.Message):
  """A DeviceStateDetails object.

  Fields:
    errorDetails: A string attribute.
    progressDetails: A string attribute.
  """

  errorDetails = messages.StringField(1)
  progressDetails = messages.StringField(2)


class Distribution(messages.Message):
  """A Distribution object.

  Fields:
    marketShare: A number attribute.
    measurementTime: A string attribute.
  """

  marketShare = messages.FloatField(1)
  measurementTime = messages.StringField(2)


class Empty(messages.Message):
  """A Empty object."""


class Environment(messages.Message):
  """A Environment object.

  Fields:
    androidDevice: A AndroidDevice attribute.
  """

  androidDevice = messages.MessageField('AndroidDevice', 1)


class EnvironmentMatrix(messages.Message):
  """A EnvironmentMatrix object.

  Fields:
    androidMatrix: A AndroidMatrix attribute.
  """

  androidMatrix = messages.MessageField('AndroidMatrix', 1)


class FileReference(messages.Message):
  """A FileReference object.

  Fields:
    blob: A BlobstoreFile attribute.
    gcsPath: A string attribute.
  """

  blob = messages.MessageField('BlobstoreFile', 1)
  gcsPath = messages.StringField(2)


class GceInstanceDetails(messages.Message):
  """A GceInstanceDetails object.

  Fields:
    name: A string attribute.
    projectId: A string attribute.
    zone: A string attribute.
  """

  name = messages.StringField(1)
  projectId = messages.StringField(2)
  zone = messages.StringField(3)


class GoogleCloudStorage(messages.Message):
  """A GoogleCloudStorage object.

  Fields:
    gcsPath: A string attribute.
  """

  gcsPath = messages.StringField(1)


class LinuxMachineCatalog(messages.Message):
  """A LinuxMachineCatalog object.

  Fields:
    versions: A LinuxVersion attribute.
  """

  versions = messages.MessageField('LinuxVersion', 1, repeated=True)


class LinuxVersion(messages.Message):
  """A LinuxVersion object.

  Fields:
    id: A string attribute.
    versionString: A string attribute.
  """

  id = messages.StringField(1)
  versionString = messages.StringField(2)


class ListDevicesResponse(messages.Message):
  """A ListDevicesResponse object.

  Fields:
    devices: A Device attribute.
    nextPageToken: A string attribute.
  """

  devices = messages.MessageField('Device', 1, repeated=True)
  nextPageToken = messages.StringField(2)


class ListTestExecutionsResponse(messages.Message):
  """A ListTestExecutionsResponse object.

  Fields:
    testExecutions: A TestExecution attribute.
  """

  testExecutions = messages.MessageField('TestExecution', 1, repeated=True)


class ListTestMatricesResponse(messages.Message):
  """A ListTestMatricesResponse object.

  Fields:
    testMatrices: A TestMatrix attribute.
  """

  testMatrices = messages.MessageField('TestMatrix', 1, repeated=True)


class Locale(messages.Message):
  """A Locale object.

  Fields:
    id: A string attribute.
    name: A string attribute.
    region: A string attribute.
    tags: A string attribute.
  """

  id = messages.StringField(1)
  name = messages.StringField(2)
  region = messages.StringField(3)
  tags = messages.StringField(4, repeated=True)


class Orientation(messages.Message):
  """A Orientation object.

  Fields:
    id: A string attribute.
    name: A string attribute.
    tags: A string attribute.
  """

  id = messages.StringField(1)
  name = messages.StringField(2)
  tags = messages.StringField(3, repeated=True)


class ResultStorage(messages.Message):
  """A ResultStorage object.

  Fields:
    googleCloudStorage: A GoogleCloudStorage attribute.
    toolResultsExecutionId: A string attribute.
    toolResultsHistoryId: A string attribute.
    toolResultsStepId: A string attribute.
  """

  googleCloudStorage = messages.MessageField('GoogleCloudStorage', 1)
  toolResultsExecutionId = messages.StringField(2)
  toolResultsHistoryId = messages.StringField(3)
  toolResultsStepId = messages.StringField(4)


class StandardQueryParameters(messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = messages.StringField(2)
  key = messages.StringField(3)
  oauth_token = messages.StringField(4)
  prettyPrint = messages.BooleanField(5, default=True)
  quotaUser = messages.StringField(6)
  trace = messages.StringField(7)
  userIp = messages.StringField(8)


class TestDetails(messages.Message):
  """A TestDetails object.

  Fields:
    errorDetails: A string attribute.
    progressDetails: A string attribute.
  """

  errorDetails = messages.StringField(1)
  progressDetails = messages.StringField(2)


class TestEnvironmentCatalog(messages.Message):
  """A TestEnvironmentCatalog object.

  Fields:
    androidDeviceCatalog: A AndroidDeviceCatalog attribute.
    webDriverCatalog: A WebDriverCatalog attribute.
  """

  androidDeviceCatalog = messages.MessageField('AndroidDeviceCatalog', 1)
  webDriverCatalog = messages.MessageField('WebDriverCatalog', 2)


class TestExecution(messages.Message):
  """A TestExecution object.

  Enums:
    StateValueValuesEnum:

  Fields:
    environment: A Environment attribute.
    id: A string attribute.
    matrixId: A string attribute.
    projectId: A string attribute.
    resultStorage: A ResultStorage attribute.
    state: A StateValueValuesEnum attribute.
    testDetails: A TestDetails attribute.
    testSpecification: A TestSpecification attribute.
    timestamp: A string attribute.
  """

  class StateValueValuesEnum(messages.Enum):
    """StateValueValuesEnum enum type.

    Values:
      CANCELLED: <no description>
      ERROR: <no description>
      FINISHED: <no description>
      INVALID: <no description>
      IN_PROGRESS: <no description>
      PENDING: <no description>
      QUEUED: <no description>
      RUNNING: <no description>
      UNSPECIFIED_TEST_STATE: <no description>
      UNSUPPORTED_ENVIRONMENT: <no description>
      VALIDATING: <no description>
    """
    CANCELLED = 0
    ERROR = 1
    FINISHED = 2
    INVALID = 3
    IN_PROGRESS = 4
    PENDING = 5
    QUEUED = 6
    RUNNING = 7
    UNSPECIFIED_TEST_STATE = 8
    UNSUPPORTED_ENVIRONMENT = 9
    VALIDATING = 10

  environment = messages.MessageField('Environment', 1)
  id = messages.StringField(2)
  matrixId = messages.StringField(3)
  projectId = messages.StringField(4)
  resultStorage = messages.MessageField('ResultStorage', 5)
  state = messages.EnumField('StateValueValuesEnum', 6)
  testDetails = messages.MessageField('TestDetails', 7)
  testSpecification = messages.MessageField('TestSpecification', 8)
  timestamp = messages.StringField(9)


class TestMatrix(messages.Message):
  """A TestMatrix object.

  Enums:
    StateValueValuesEnum:

  Fields:
    clientInfo: A ClientInfo attribute.
    environmentMatrix: A EnvironmentMatrix attribute.
    projectId: A string attribute.
    resultStorage: A ResultStorage attribute.
    state: A StateValueValuesEnum attribute.
    testExecutions: A TestExecution attribute.
    testMatrixId: A string attribute.
    testSpecification: A TestSpecification attribute.
    timestamp: A string attribute.
  """

  class StateValueValuesEnum(messages.Enum):
    """StateValueValuesEnum enum type.

    Values:
      CANCELLED: <no description>
      ERROR: <no description>
      FINISHED: <no description>
      INVALID: <no description>
      IN_PROGRESS: <no description>
      PENDING: <no description>
      QUEUED: <no description>
      RUNNING: <no description>
      UNSPECIFIED_TEST_STATE: <no description>
      UNSUPPORTED_ENVIRONMENT: <no description>
      VALIDATING: <no description>
    """
    CANCELLED = 0
    ERROR = 1
    FINISHED = 2
    INVALID = 3
    IN_PROGRESS = 4
    PENDING = 5
    QUEUED = 6
    RUNNING = 7
    UNSPECIFIED_TEST_STATE = 8
    UNSUPPORTED_ENVIRONMENT = 9
    VALIDATING = 10

  clientInfo = messages.MessageField('ClientInfo', 1)
  environmentMatrix = messages.MessageField('EnvironmentMatrix', 2)
  projectId = messages.StringField(3)
  resultStorage = messages.MessageField('ResultStorage', 4)
  state = messages.EnumField('StateValueValuesEnum', 5)
  testExecutions = messages.MessageField('TestExecution', 6, repeated=True)
  testMatrixId = messages.StringField(7)
  testSpecification = messages.MessageField('TestSpecification', 8)
  timestamp = messages.StringField(9)


class TestSpecification(messages.Message):
  """A TestSpecification object.

  Fields:
    androidInstrumentationTest: A AndroidInstrumentationTest attribute.
    androidMonkeyTest: A AndroidMonkeyTest attribute.
    androidRoboTest: A AndroidRoboTest attribute.
    testTimeout: A string attribute.
  """

  androidInstrumentationTest = messages.MessageField('AndroidInstrumentationTest', 1)
  androidMonkeyTest = messages.MessageField('AndroidMonkeyTest', 2)
  androidRoboTest = messages.MessageField('AndroidRoboTest', 3)
  testTimeout = messages.StringField(4)


class TestingProjectsDeviceDeleteRequest(messages.Message):
  """A TestingProjectsDeviceDeleteRequest object.

  Fields:
    deviceId: A string attribute.
    projectId: A string attribute.
  """

  deviceId = messages.StringField(1, required=True)
  projectId = messages.StringField(2, required=True)


class TestingProjectsDevicesCreateRequest(messages.Message):
  """A TestingProjectsDevicesCreateRequest object.

  Fields:
    device: A Device resource to be passed as the request body.
    projectId: A string attribute.
  """

  device = messages.MessageField('Device', 1)
  projectId = messages.StringField(2, required=True)


class TestingProjectsDevicesGetRequest(messages.Message):
  """A TestingProjectsDevicesGetRequest object.

  Fields:
    deviceId: A string attribute.
    projectId: A string attribute.
  """

  deviceId = messages.StringField(1, required=True)
  projectId = messages.StringField(2, required=True)


class TestingProjectsDevicesKeepaliveRequest(messages.Message):
  """A TestingProjectsDevicesKeepaliveRequest object.

  Fields:
    deviceId: A string attribute.
    projectId: A string attribute.
  """

  deviceId = messages.StringField(1, required=True)
  projectId = messages.StringField(2, required=True)


class TestingProjectsDevicesListRequest(messages.Message):
  """A TestingProjectsDevicesListRequest object.

  Fields:
    pageSize: A integer attribute.
    pageToken: A string attribute.
    projectId: A string attribute.
  """

  pageSize = messages.IntegerField(1, variant=messages.Variant.INT32)
  pageToken = messages.StringField(2)
  projectId = messages.StringField(3, required=True)


class TestingProjectsTestExecutionsCancelRequest(messages.Message):
  """A TestingProjectsTestExecutionsCancelRequest object.

  Fields:
    projectId: A string attribute.
    testExecutionId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testExecutionId = messages.StringField(2, required=True)


class TestingProjectsTestExecutionsCreateRequest(messages.Message):
  """A TestingProjectsTestExecutionsCreateRequest object.

  Fields:
    projectId: A string attribute.
    testExecution: A TestExecution resource to be passed as the request body.
  """

  projectId = messages.StringField(1, required=True)
  testExecution = messages.MessageField('TestExecution', 2)


class TestingProjectsTestExecutionsDeleteRequest(messages.Message):
  """A TestingProjectsTestExecutionsDeleteRequest object.

  Fields:
    projectId: A string attribute.
    testExecutionId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testExecutionId = messages.StringField(2, required=True)


class TestingProjectsTestExecutionsGetRequest(messages.Message):
  """A TestingProjectsTestExecutionsGetRequest object.

  Fields:
    projectId: A string attribute.
    testExecutionId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testExecutionId = messages.StringField(2, required=True)


class TestingProjectsTestExecutionsListRequest(messages.Message):
  """A TestingProjectsTestExecutionsListRequest object.

  Fields:
    projectId: A string attribute.
    query: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  query = messages.StringField(2)


class TestingProjectsTestMatricesCancelRequest(messages.Message):
  """A TestingProjectsTestMatricesCancelRequest object.

  Fields:
    projectId: A string attribute.
    testMatrixId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testMatrixId = messages.StringField(2, required=True)


class TestingProjectsTestMatricesCreateRequest(messages.Message):
  """A TestingProjectsTestMatricesCreateRequest object.

  Fields:
    projectId: A string attribute.
    testMatrix: A TestMatrix resource to be passed as the request body.
  """

  projectId = messages.StringField(1, required=True)
  testMatrix = messages.MessageField('TestMatrix', 2)


class TestingProjectsTestMatricesDeleteRequest(messages.Message):
  """A TestingProjectsTestMatricesDeleteRequest object.

  Fields:
    projectId: A string attribute.
    testMatrixId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testMatrixId = messages.StringField(2, required=True)


class TestingProjectsTestMatricesGetRequest(messages.Message):
  """A TestingProjectsTestMatricesGetRequest object.

  Fields:
    projectId: A string attribute.
    testMatrixId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)
  testMatrixId = messages.StringField(2, required=True)


class TestingProjectsTestMatricesListRequest(messages.Message):
  """A TestingProjectsTestMatricesListRequest object.

  Fields:
    projectId: A string attribute.
  """

  projectId = messages.StringField(1, required=True)


class TestingTestEnvironmentCatalogGetRequest(messages.Message):
  """A TestingTestEnvironmentCatalogGetRequest object.

  Enums:
    EnvironmentTypeValueValuesEnum:

  Fields:
    environmentType: A EnvironmentTypeValueValuesEnum attribute.
  """

  class EnvironmentTypeValueValuesEnum(messages.Enum):
    """EnvironmentTypeValueValuesEnum enum type.

    Values:
      ANDROID: <no description>
      UNSPECIFIED: <no description>
      WEBDRIVER: <no description>
    """
    ANDROID = 0
    UNSPECIFIED = 1
    WEBDRIVER = 2

  environmentType = messages.EnumField('EnvironmentTypeValueValuesEnum', 1, required=True)


class WebDriverCatalog(messages.Message):
  """A WebDriverCatalog object.

  Fields:
    browsers: A Browser attribute.
  """

  browsers = messages.MessageField('Browser', 1, repeated=True)


class WindowsMachineCatalog(messages.Message):
  """A WindowsMachineCatalog object.

  Fields:
    versions: A WindowsVersion attribute.
  """

  versions = messages.MessageField('WindowsVersion', 1, repeated=True)


class WindowsVersion(messages.Message):
  """A WindowsVersion object.

  Fields:
    id: A string attribute.
    versionString: A string attribute.
  """

  id = messages.StringField(1)
  versionString = messages.StringField(2)


